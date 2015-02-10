

module jazzy.Interperter {
    export interface GenericInterperter {
        CreateScope: Function;
        DestroyScope: Function;
        GoTo: Function;
    }

    export class Interperter<T> {
        private _scopes: structure.StackList<Scope<T>>;
        private _lables: structure.HashTable<number>;
        private _functions: structure.HashTable<Funcs.JazFunc>;
        private _program: string[];
        private _curScope: Scope<T>;

        constructor() {
            this._program = [];
            this._scopes = new structure.StackList<Scope<T>>();
            this._lables = new structure.HashTable<number>();
            this._functions = new structure.HashTable<Funcs.JazFunc>();
            this._curScope = new Scope<T>();
            this._scopes.Push(this._curScope);
        }

        public CreateScope(): Scope<T> {
            this._scopes.Push(new Scope<T>(this._curScope.PC()));
            return this._scopes.Get(0);
        }

        public DestroyTopScope(): Scope<T> {
            var old = this._scopes.Pop();
            this._curScope = this._scopes.Get(0);
            return old;
        }

        public GoTo(line: number) {
            if (line < this._program.length) {
                this._curScope.PC(line);
            }
        }

        public Exec(instruction: string) {

        }




    }
}
