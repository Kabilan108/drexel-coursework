clasdef person < handle
    properties (SetAccess = protected)
        name
    end

    properties
        age
        zipcode
    end

    properties (Dependent)
        birthyear
    end

    methods
        function p = person(inname, inage, inzipcode)
            if ~exist('inname','var'); inname='Unknown Person'; end
            p.name = inname;
            p.age = inage;
            p.zipcode = inzipcode;

        end

        function q = incrementage( p, byhowmuch )
            if ~exist('byhowmuch','var'); byhowmuch=1; end
            if nargout
                q = person(p.name, p.age, p.zipcode);
            else
                q = p;
            end
            q.age = q.age +1;
        end

        function out = get.birthyear(p)
            now = clock;
            out = now(1) - p.age;
        end

        function p = set.birthyear(p, newbirthyear)
            now = clock;
            p.age = now(1) - newbirthyear;
        end

        function disp( p )
            % fprintf('Person: %s (%d) from zipcode:%d\n', p.name, p.age, p.zipcode);
            x = struct('name', p.name, 'age',p.age);
            disp(x);
        end
    end

ends
