package com.microsoft.azure.cosmosdb.internal.routing;

import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class StringPartitionKeyComponentTest {
    @DataProvider(name = "paramProvider")
    public Object[][] paramProvider() {
        return new Object[][] {
                {"Friday", "Friday", 0},
                {"Friday", "Venerdì", -1},
                {"Fri", "Ven", -1},
        };
    }

    @Test(groups = { "unit" }, dataProvider = "paramProvider")
    public void compare(String str1, String str2, int expectedCompare) {
        StringPartitionKeyComponent spkc1 = new StringPartitionKeyComponent(str1);
        StringPartitionKeyComponent spkc2 = new StringPartitionKeyComponent(str2);

        assertThat(Integer.signum(spkc1.CompareTo(spkc2))).isEqualTo(Integer.signum(expectedCompare));
    }


    @Test(groups = {"unit"})
    public void getIssue56() {
        String partition = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        StringPartitionKeyComponent spkc1 = new StringPartitionKeyComponent(partition);

        Assert.assertTrue(spkc1.MAX_STRING_BYTES_TO_APPEND >= partition.length());
    }
}
