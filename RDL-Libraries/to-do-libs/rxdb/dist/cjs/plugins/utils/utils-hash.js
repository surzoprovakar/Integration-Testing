"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.defaultHashSha256 = exports.canUseCryptoSubtle = void 0;
exports.jsSha256 = jsSha256;
exports.nativeSha256 = nativeSha256;
var _ohash = require("ohash");
var crypto = _interopRequireWildcard(require("crypto"));
function _getRequireWildcardCache(e) { if ("function" != typeof WeakMap) return null; var r = new WeakMap(), t = new WeakMap(); return (_getRequireWildcardCache = function (e) { return e ? t : r; })(e); }
function _interopRequireWildcard(e, r) { if (!r && e && e.__esModule) return e; if (null === e || "object" != typeof e && "function" != typeof e) return { default: e }; var t = _getRequireWildcardCache(r); if (t && t.has(e)) return t.get(e); var n = { __proto__: null }, a = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var u in e) if ("default" !== u && {}.hasOwnProperty.call(e, u)) { var i = a ? Object.getOwnPropertyDescriptor(e, u) : null; i && (i.get || i.set) ? Object.defineProperty(n, u, i) : n[u] = e[u]; } return n.default = e, t && t.set(e, n), n; }
/**
 * TODO in the future we should no longer provide a
 * fallback to crypto.subtle.digest.
 * Instead users without crypto.subtle.digest support, should have to provide their own
 * hash function.
 */
function jsSha256(input) {
  return Promise.resolve((0, _ohash.sha256)(input));
}
async function nativeSha256(input) {
  var data = new TextEncoder().encode(input);
  var hashBuffer = await crypto.subtle.digest('SHA-256', data);
  /**
   * @link https://jameshfisher.com/2017/10/30/web-cryptography-api-hello-world/
   */
  var hash = Array.prototype.map.call(new Uint8Array(hashBuffer), x => ('00' + x.toString(16)).slice(-2)).join('');
  return hash;
}
var canUseCryptoSubtle = exports.canUseCryptoSubtle = typeof crypto !== 'undefined' && typeof crypto.subtle !== 'undefined' && typeof crypto.subtle.digest === 'function';

/**
 * Default hash method used to hash
 * strings and do equal comparisons.
 *
 * IMPORTANT: Changing the default hashing method
 * requires a BREAKING change!
 */

var defaultHashSha256 = exports.defaultHashSha256 = canUseCryptoSubtle ? nativeSha256 : jsSha256;
//# sourceMappingURL=utils-hash.js.map