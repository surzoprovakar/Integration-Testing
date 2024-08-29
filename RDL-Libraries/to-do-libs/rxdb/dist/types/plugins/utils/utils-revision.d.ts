import type { RxDocumentData } from '../../types/index.d.ts';
export declare function parseRevision(revision: string): {
    height: number;
    hash: string;
};
/**
 * @hotPath
 */
export declare function getHeightOfRevision(revision: string): number;
/**
 * Creates the next write revision for a given document.
 */
export declare function createRevision<RxDocType>(databaseInstanceToken: string, previousDocData?: RxDocumentData<RxDocType>): string;
