---
title: Memory RxStorage
slug: rx-storage-memory.html
---

# Memory RxStorage

<!-- keywords:
javascript in-memory database
in memory db
node js in memory database
in memory storage
Nestjs in-memory database

-->

The Memory `RxStorage` is based on plain in memory arrays and objects. It can be used in all environments and is made for performance.
Use this storage when you need a really fast database like in your unit tests or when you use RxDB with server side rendering.

### Pros

- Really fast. Uses binary search on all operations.
- Small build size

### Cons

- No persistence


```ts
import {
    createRxDatabase
} from 'rxdb';
import {
    getRxStorageMemory
} from 'rxdb/plugins/storage-memory';

const db = await createRxDatabase({
    name: 'exampledb',
    storage: getRxStorageMemory()
});
```
