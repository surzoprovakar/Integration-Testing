/**
 * this plugin allows delta-updates with mongo-like-syntax
 * It's using mingo internally
 * @link https://github.com/kofrasa/mingo
 */

import { mingoUpdater } from "./mingo-updater.js";
export function incrementalUpdate(updateObj) {
  return this.incrementalModify(docData => {
    var newDocData = mingoUpdater(docData, updateObj);
    return newDocData;
  });
}
export function update(updateObj) {
  var oldDocData = this._data;
  var newDocData = mingoUpdater(oldDocData, updateObj);
  return this._saveData(newDocData, oldDocData);
}
export function RxQueryUpdate(updateObj) {
  return this.exec().then(docs => {
    if (!docs) {
      return null;
    }
    if (Array.isArray(docs)) {
      return Promise.all(docs.map(doc => doc.update(updateObj))).then(() => docs);
    } else {
      // via findOne()
      return docs.update(updateObj).then(() => docs);
    }
  });
}
export var RxDBUpdatePlugin = {
  name: 'update',
  rxdb: true,
  prototypes: {
    RxDocument: proto => {
      proto.update = update;
      proto.incrementalUpdate = incrementalUpdate;
    },
    RxQuery: proto => {
      proto.update = RxQueryUpdate;
    }
  }
};
//# sourceMappingURL=index.js.map