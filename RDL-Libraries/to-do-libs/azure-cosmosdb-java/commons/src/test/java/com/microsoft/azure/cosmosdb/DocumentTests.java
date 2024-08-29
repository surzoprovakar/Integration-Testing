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

import static org.assertj.core.api.Assertions.assertThat;

import java.util.Date;
import java.util.UUID;

import org.testng.Assert;
import org.testng.annotations.Test;

public class DocumentTests {

    @Test(groups = { "unit" })
    public void timestamp()  {
        Document d = new Document();
        Date time = new Date(86400 * 1000);
        d.setTimestamp(time);
        assertThat(d.getTimestamp()).isEqualTo(time);
    }

    @Test(groups = { "unit" })
    public void documentSizeIssue33()  {
        int desiredSizeInBytes = 2 * 1024 * 1024;

        StringBuilder stringBuilder = new StringBuilder();
        while (stringBuilder.length() < desiredSizeInBytes) {
            stringBuilder.append(UUID.randomUUID().toString());
        }

        String uuid = stringBuilder.toString();
        Document doc = new Document(String.format("{ "
                + "\"id\": \"%s\", "
                + "\"mypk\": \"%s\", "
                + "\"sgmts\": [[6519456, 1471916863], [2498434, 1455671440]]"
                + "}"
                , uuid, uuid));
        Assert.assertTrue(doc.toJson().length() >= 2048);
        Assert.assertTrue(doc.toJson().length() <= 2048);
    }
}
