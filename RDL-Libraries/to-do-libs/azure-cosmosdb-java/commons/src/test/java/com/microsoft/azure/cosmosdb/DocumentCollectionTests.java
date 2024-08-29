/*
 * The MIT License (MIT)
 * Copyright (c) 2018 Microsoft Corporation
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package com.microsoft.azure.cosmosdb;

import com.google.common.collect.ImmutableList;

import org.testng.Assert;
import org.testng.annotations.Test;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.Arrays;
import java.util.Collections;

public class DocumentCollectionTests {

    private static final String DATABASE = "test_db";
    private static final String COLLECTION = "test_coll";

    @Test(groups = { "unit" })
    public void getPartitionKey() {
        DocumentCollection collection = new DocumentCollection();
        PartitionKeyDefinition partitionKeyDefinition = new PartitionKeyDefinition();
        partitionKeyDefinition.setPaths(ImmutableList.of("/mypk"));
        collection.setPartitionKey(partitionKeyDefinition);
        assertThat(collection.getPartitionKey()).isEqualTo(partitionKeyDefinition);
    }

    @Test(groups = { "unit" })
    public void getPartitionKey_serializeAndDeserialize() {
        DocumentCollection collection = new DocumentCollection();
        PartitionKeyDefinition partitionKeyDefinition = new PartitionKeyDefinition();
        partitionKeyDefinition.setPaths(ImmutableList.of("/mypk"));
        partitionKeyDefinition.setVersion(PartitionKeyDefinitionVersion.V2);
        collection.setPartitionKey(partitionKeyDefinition);

        DocumentCollection parsedColl = new DocumentCollection(collection.toJson());
        assertThat(parsedColl.getPartitionKey().getKind().toString())
                .isEqualTo(partitionKeyDefinition.getKind().toString());
        assertThat(parsedColl.getPartitionKey().getPaths()).isEqualTo(partitionKeyDefinition.getPaths());
        assertThat(parsedColl.getPartitionKey().getVersion()).isEqualTo(partitionKeyDefinition.getVersion());
    }

    @Test(groups = { "unit" })
    public void getIndexingPolicy() {
        DocumentCollection collection = new DocumentCollection();
        assertThat(collection.getIndexingPolicy().getCompositeIndexes()).isNotNull();
    }

    @Test(groups = { "unit" })
    public void getIssue93() {
        DocumentCollection documentCollection = new DocumentCollection();
        documentCollection.setId(COLLECTION);
        IndexingPolicy indexingPolicy = new IndexingPolicy();
        indexingPolicy.setIndexingMode(IndexingMode.Consistent);
        IncludedPath includedPath = new IncludedPath();
        includedPath.setPath("/*");
        Index numberIndex = Index.Range(DataType.Number, -1);
        Index stringIndex = Index.Range(DataType.String);
        includedPath.setIndexes(Arrays.asList(numberIndex, stringIndex));
        indexingPolicy.setIncludedPaths(Collections.singletonList(includedPath));
        documentCollection.setIndexingPolicy(indexingPolicy);

        Assert.assertTrue(documentCollection.getIndexingPolicy().getIndexingMode() == IndexingMode.Consistent);

        assertThat(documentCollection.getIndexingPolicy()).isNotNull();
        Assert.assertTrue(documentCollection.getIndexingPolicy() == new IndexingPolicy("{true,Consistent}"));
    }

}
