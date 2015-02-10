/// <reference path="../Structures/hashtable.ts" />
/// <reference path="../Structures/stacklist.ts" />


module jazzy.Interperter {
    export class Scope<T>{
        private _pc: number;
        private _variables: structure.HashTable<T>;
        private _lvalue: Scope<T>;
        private _rvalue: Scope<T>;
        private _stack: structure.StackList<T>;

    constructor(){
      this.pc = 0;
      this.variables = new Structure.HashTable<T>();
      this.stack =  new Structure.StackList<T>();
    }

        constructor(pc?: number) {
            this._pc = pc || 0;
            this._variables = new structure.HashTable<T>();
            this._stack = new structure.StackList<T>();
            this._lvalue = this;
            this._rvalue = this;
        }

        public GetVar(name: string): T {
            if (this._variables.Contains(name))
                return this._variables.Get(name);
            else
                return null;
        }

        public SetVar(name: string, value: T): void {
            this._variables.Set(name, value);
        }

        public Step(): void {
            this._pc++;
        }

        public PC(val?: number): number {
            if (typeof val != "undefined") {
                this._pc = val;
            }
            return this._pc;
        }

        public Stack(): structure.StackList<T> {
            return this._stack;
        }

        public LValue(scope?: Scope<T>): Scope<T> {
            if (typeof scope != "undefined") {
                this._lvalue = scope;
            }
            return this._lvalue;
        }

        public RValue(scope?: Scope<T>): Scope<T> {
            if (typeof scope != "undefined") {
                this._rvalue = scope;
            }
            return this._rvalue;
        }
    }
}
